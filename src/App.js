import {  Ticker, Chart, Insights, Input } from './components'
import './App.css'

const App = () => {
  return (
    <div>
      <div >
        <Ticker />
        <hr></hr>
      </div>
      <div>
        <div>
          <Chart />
        </div>
        <div>
          <Input />
        </div>
      </div>
      <div>
        <hr></hr>
        <Insights />
      </div>
    </div>
  )
}

export default App