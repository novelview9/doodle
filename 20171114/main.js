import { PythagorasTree } from './PythagorasTree.js'

ReactDOM.render(
  <PythagorasTree
    // Try changing `sprout` from 0.01 to 0.2
    sprout={0.01}

    // Try changing `sway` from 0.04 to 0.3
    sway={0.04}
  />
  ,
  document.getElementById('app')
)
