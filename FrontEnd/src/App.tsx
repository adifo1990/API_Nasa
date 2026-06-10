import { useState } from 'react'
import './App.css'
import Cartao_neo from './cartoes/neo/cartao_neo'
import Cartao_apod from './cartoes/apod/cartao_apod';

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
    </>
  )
}

export default App
