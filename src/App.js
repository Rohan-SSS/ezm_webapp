import {  Ticker, Chart, Insights, Input } from './components'
import './App.css'

const App = () => {
  return (
    <div className='App'>
      <div >
        <Ticker />
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
        <Insights />
      </div>
    </div>
  )
}

export default App