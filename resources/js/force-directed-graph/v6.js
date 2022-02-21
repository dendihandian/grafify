const data = (typeof t_graph_data) != 'undefined' ? t_graph_data : false;
const is_graph_page = (typeof t_is_graph_page) != 'undefined' ? t_is_graph_page : false;
const nodes_color = (typeof t_nodes_color) != 'undefined' ? t_nodes_color : "#14B8A6";
const edges_color = (typeof t_edges_color) != 'undefined' ? t_edges_color : "#16A34A";
const nodes_size = (typeof t_nodes_size) != 'undefined' ? t_nodes_size : 5;
const edges_size = (typeof t_edges_size) != 'undefined' ? t_edges_size : 2;

import * as d3 from "d3";

if (data) {
    const drag = simulation => {
        function dragstarted(event) {
            if (!event.active) simulation.alphaTarget(0.3).restart();
            event.subject.fx = event.subject.x;
            event.subject.fy = event.subject.y;
        }
        function dragged(event) {
            event.subject.fx = event.x;
            event.subject.fy = event.y;
        }
        function dragended(event) {
            if (!event.active) simulation.alphaTarget(0);
            event.subject.fx = null;
            event.subject.fy = null;
        }
        return d3.drag().on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended);
    }

    const color = () => {
        const scale = d3.scaleOrdinal(d3.schemeCategory10);
        return d => scale(d.group);
    }

    let width = screen.width * 0.95;
    let height = screen.height * 0.55;

    if (is_graph_page) {
        width = screen.width * 0.45;
        height = screen.height * 0.30;
    }

    const links = data.edges.map(d => Object.create(d));
    const nodes = data.nodes.map(d => Object.create(d));

    const simulation = d3.forceSimulation(nodes)
        .force("link", d3.forceLink(links).id(d => d.id))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2));

    const svg = d3.select("#graph-container").append("svg")
        .attr('width', width)
        .attr('height', height);

    const link = svg.append("g")
        .attr("stroke", edges_color)
        .attr("stroke-opacity", 0.6)
        .selectAll("line")
        .data(links)
        .join("line")
        // .attr("stroke-width", d => Math.sqrt(d.value));
        .attr("stroke-width", edges_size);

    const node = svg.append("g")
        .attr("stroke", "#fff")
        .attr("stroke-width", 1.5)
        .selectAll("circle")
        .data(nodes)
        .join("circle")
        .attr("fill", nodes_color);


    if (data['centrality']) {
        node.attr("r", d => nodes_size + (data['centrality'][d.id] * 10))
    } else {
        node.attr("r", nodes_size)
    }

    node.call(drag(simulation));

    node.append("title")
        .text(d => d.id);

    simulation.on("tick", () => {
        link.attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node.attr("cx", d => d.x)
            .attr("cy", d => d.y);
    });
}

