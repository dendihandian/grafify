// console.log('graph initidated');
// console.log(graph_data);
// console.log('nodes_size', nodes_size);
// console.log('nodes_color', nodes_color);
// console.log('edges_size', edges_size);
// console.log('edges_color', edges_color);

const data = (typeof graph_data) != 'undefined' ? graph_data : false;
const nodes_size = (typeof nodes_size) != 'undefined' ? nodes_size : 5;
const nodes_color = (typeof nodes_color) != 'undefined' ? nodes_color : '#2C7A7B';
const edges_size = (typeof edges_size) != 'undefined' ? edges_size : 2;
const edges_color = (typeof edges_color) != 'undefined' ? edges_color : '#A0AEC0';

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
    
    return d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
  }

  const color = () => {
    const scale = d3.scaleOrdinal(d3.schemeCategory10);
    return d => scale(d.group);
  }

  // const chart = () => {

    // console.log(d3.select("#graph-container").node().getBBox());

    const width = screen.width * 1;
    const height = screen.height * 0.55;

    const links = data.edges.map(d => Object.create(d));
    const nodes = data.nodes.map(d => Object.create(d));

    const simulation = d3.forceSimulation(nodes)
        .force("link", d3.forceLink(links).id(d => d.id))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2));

  //   const svg = d3.create("svg")
  //       .attr("viewBox", [0, 0, width, height]);

    // console.log('width', width);
    // console.log('height', height);

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
        .attr("r", nodes_size)
        .attr("fill", nodes_color)
        .call(drag(simulation));

    node.append("title")
        .text(d => d.id);

    simulation.on("tick", () => {
      link
          .attr("x1", d => d.source.x)
          .attr("y1", d => d.source.y)
          .attr("x2", d => d.target.x)
          .attr("y2", d => d.target.y);

      node
          .attr("cx", d => d.x)
          .attr("cy", d => d.y);
    });

  //   invalidation.then(() => simulation.stop());

  //   return svg.node();
  // }

  // chart();
}

