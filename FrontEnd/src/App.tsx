import { useState } from 'react'
import './App.css'

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

      <section id='next-steps'>
        <div id='social'>
          <h2>APOD</h2>
          <p>Um dos sites mais populares da NASA é o Astronomy Picture of the Day. Na verdade, este site é um dos mais populares em todas as agências federais. Tem o apelo popular de um vídeo de Justin Bieber. Esse endpoint estrutura as imagens APOD e os metadados associados para que possam ser reaproveitados para outras aplicações. Além disso, se o parâmetro for definido para , então as palavras-chave derivadas da explicação da imagem são retornadas. Essas palavras-chave podiam ser usadas como hashtags geradas automaticamente para feeds do Twitter ou Instagram; mas geralmente ajudam na descoberta de imagens relevantes.</p>
          
          
          <ul>
            <h3>Modo de pesquisa:</h3>
            <li>
              <input type='radio' value='data' name='ModoApod' />
              <label>-Data</label>
            </li>
            <li>
              <input type='radio' value='intervalo' name='ModoApod' />
              <label>-Intervalo</label>
            </li>
            <li>
              <input type='radio' value='quantidade' name='ModoApod' />
              <label>-Quantidade</label>
            </li>
            <li>
              <input type='radio' value='url' name='ModoApod' />
              <label htmlFor="url">-URL</label>
            </li>
          </ul>
          <ul>
            <li>
              <a href="https://github.com/vitejs/vite" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#github-icon"></use>
                </svg>
                GitHub
              </a>
              <form>
                <p>Pesquisa por Data</p>

                <label htmlFor='data_unica'>Data*</label>
	              <input type='date' id='data_unica' name='data_unica' required />

                <input type='submit' value='Buscar' />
              </form>
            </li>

            <li>
              <form>
                <p>Pesquisa por Intervalo</p>

                <label htmlFor='data_inicial'>Data Incial*</label>
	              <input type='date' id='data_inicial' name='data_inicial' required />

                <label htmlFor="data_final">Data Final*</label>
	              <input type='date' id='data_final' name='data_final' required />

                <input type='submit' value='Buscar' />
              </form>
            </li>

            <li>
              <form>
                <p>Pesquisa por Quantidade</p>

                <label htmlFor='quantidade_apod'>Quantidade*</label>
                <input type='number' id='quantidade_apod' placeholder='1' required />

                <input type='submit' value='Buscar' />
              </form>
            </li>

            <li>
              <form>
                <p>Pesquisa por URL</p>

                <label htmlFor='url_apod'>URL*</label>
                <input type='url' id='url_apod' placeholder='https://...' required />
 
                <input type='submit' value='Buscar' />
              </form>
            </li>
          </ul>
        </div>
      </section>

      <div className='separacao'></div>
    </>
  )
}

export default App
