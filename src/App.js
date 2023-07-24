import { Navbar, Chart, Insights } from './components'
import './App.css'

const App = () => {
  return (
    <div className='App'>
      <div>
        <div className='navbar'>
          <Navbar />
        </div>
        <div className='chart'>
          <Chart />
        </div>
      </div>
      <div>
        <Insights />
      </div>
    </div>
  )
}

export default App