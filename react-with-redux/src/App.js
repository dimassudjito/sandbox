import logo from './logo.svg'
import './App.css'
import { useSelector, useDispatch } from 'react-redux'
import { bindActionCreators } from 'redux'
import { actionCreators } from './state/index'

function App() {
  // const state = useSelector((state) => state)
  const account = useSelector((state) => state.account)
  const dispatch = useDispatch()

  const { depositMoney, withdrawMoney } = bindActionCreators(
    actionCreators,
    dispatch
  )

  console.log(depositMoney)

  return (
    <div className="App">
      {account}
      <button onClick={() => depositMoney(100)}>Deposit</button>
    </div>
  )
}

export default App
