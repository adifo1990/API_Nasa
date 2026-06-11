import { useState } from 'react'
import './App.css'
import Cartao_neo from './cartoes/cartao_neo'
import Cartao_apod from './cartoes/cartao_apod'
import Cartao_donki from './cartoes/cartao_donki'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <section id='center'>
          <h1>Get started</h1>
          <p>
            Edit <code>src/App.tsx</code> and save to test <code>HMR</code>
          </p>
        <button
          type='button'
          className='counter'
          onClick={() => setCount((count) => count + 1)}
        >
          Count is {count}
        </button>
      </section>

      <div className='separacao'></div>

      <Cartao_apod></Cartao_apod>

      <div className='separacao'></div>
      
      <Cartao_neo></Cartao_neo>

      <div className='separacao'></div>

      <Cartao_donki></Cartao_donki>

      <div className='separacao'></div>



      <div className='separacao'></div>



      <div className='separacao'></div>



      <div className='separacao'></div>



      <div className='separacao'></div>
    </>
  )
}

export default App
