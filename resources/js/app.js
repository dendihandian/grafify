import './force-directed-graph/v6';

import Alpine from 'alpinejs'
import persist from '@alpinejs/persist'
import Clipboard from "@ryangjchandler/alpine-clipboard"

Alpine.plugin(persist)
Alpine.plugin(Clipboard)
Alpine.start()