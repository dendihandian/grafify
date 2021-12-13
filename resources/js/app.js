import './force-directed-graph/v6';

import Alpine from 'alpinejs'
import persist from '@alpinejs/persist'

window.Alpine = Alpine
window.persist = persist

Alpine.plugin(persist)
Alpine.start()