import { useState } from 'react'

type Modo = 'intervalo' | 'id' | 'todos'

function cartao_neo() {
    const [dataInicial, setDataInicial] = useState('')
    const [dataFinal, setDataFinal] = useState('')
    const [asteroidId, setAsteroidId] = useState('')

    const [resultado, setResultado] = useState<any>(null)
    const [erro, setErro] = useState<string | null>(null)
    const [carregando, setCarregando] = useState(false)

    const BASE_URL = 'http://localhost:3000/nasa'

    const urls: Record<Modo, string> = {
        intervalo:   `${BASE_URL}/neo/feed?start_date=${dataInicial}&end_date=${dataFinal}`,
        id: `${BASE_URL}/neo/lookup/${asteroidId}`,
        todos: `${BASE_URL}/neo/browse`,
    }

    async function buscar(e: React.FormEvent, modo: Modo) {
        e.preventDefault()
        setErro(null)
        setResultado(null)
        setCarregando(true)
        try {
            const res = await fetch(urls[modo])
            const data = await res.json()
            if (data.error) throw new Error(data.error)
            setResultado(data)
        } catch (err: any) {
            setErro(err.message || 'Erro ao buscar')
        } finally {
            setCarregando(false)
        }
    }

    return (
        <section className='cartão' id='neo'>
            <h2>Asteroids - NeoWs</h2>
            <p>RESUMO:<br />
                - Near Earth Object Web Service -NeoWs-.<br />
                - Um serviço web RESTful para informações sobre asteroides próximos à Terra.
            </p>

            <h3>Modos de pesquisa:</h3>
            <ul>
                <li>
                    <form onSubmit={e => buscar(e, 'intervalo')}>
                        <p><b>Pesquisa por Intervalo</b></p>
                        <hr />
                        <label htmlFor='neo_input_data_inicial'>Data Inicial*</label>
                        <input
                            type='date'
                            id='neo_input_data_inicial'
                            name='neo_input_data_inicial'
                            value={dataInicial}
                            onChange={e => setDataInicial(e.target.value)}
                            required
                        />
                        <label htmlFor='neo_input_data_final'>Data Final*</label>
                        <input
                            type='date'
                            id='neo_input_data_final'
                            name='neo_input_data_final'
                            value={dataFinal}
                            onChange={e => setDataFinal(e.target.value)}
                            required
                        />
                        <input type='submit' value='Buscar' />
                    </form>
                </li>

                <li>
                    <form onSubmit={e => buscar(e, 'id')}>
                        <p><b>Pesquisa por ID</b></p>
                        <hr />
                        <label htmlFor='neo_input_id'>ID*</label>
                        <input
                            type='text'
                            id='neo_input_id'
                            name='neo_input_id'
                            inputMode='numeric'
                            placeholder='2001620'
                            pattern='[0-9]{1,7}'
                            maxLength={7}
                            value={asteroidId}
                            onChange={e => setAsteroidId(e.target.value)}
                            required
                        />
                        <input type='submit' value='Buscar' />
                    </form>
                </li>

                <li>
                    <form onSubmit={e => buscar(e, 'todos')}>
                        <p><b>Listar todos</b></p>
                        <hr />
                        <input type='submit' value='Buscar' />
                    </form>
                </li>
            </ul>

            <div id='resposta'>
                {carregando && <p>Carregando...</p>}
                {erro && <p>❌ {erro}</p>}
                {resultado && <pre>{JSON.stringify(resultado, null, 2)}</pre>}
            </div>
        </section>
    )
}

export default cartao_neo