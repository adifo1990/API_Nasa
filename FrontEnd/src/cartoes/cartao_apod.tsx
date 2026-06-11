import { useState } from 'react'

interface ApodItem {
    data: string
    titulo: string
    explicacao: string
    url: string
    media_type: string
    hdurl?: string
    thumbnail_url?: string
    copyright?: string
}

type Modo = 'data' | 'intervalo' | 'quantidade'

function cartao_apod() {
    const [dataUnica, setDataUnica] = useState('')
    const [dataInicial, setDataInicial] = useState('')
    const [dataFinal, setDataFinal] = useState('')
    const [quantidade, setQuantidade] = useState(1)

    const [resultado, setResultado] = useState<any>(null)
    const [erro, setErro] = useState<string | null>(null)
    const [carregando, setCarregando] = useState(false)

    const BASE_URL = 'http://localhost:3000/nasa'

    const urls: Record<Modo, string> = {
        data:  `${BASE_URL}/apod/photo?date=${dataUnica}`,
        intervalo: `${BASE_URL}/apod/photos?start_date=${dataInicial}&end_date=${dataFinal}`,
        quantidade:  `${BASE_URL}/apod/photos/count?count=${quantidade}`,
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

    function mostrarResposta(item: ApodItem) {
        return (
            <div key={item.data}>
                <p><b>{item.titulo} ({item.data})</b></p>
                {item.copyright && <p>© {item.copyright}</p>}
                {item.media_type === 'image' ? (
                    <img
                        src={item.url}
                        alt={item.titulo}
                    />
                ) : (
                    <iframe
                        src={item.url}
                        title={item.titulo}
                        allowFullScreen
                    />
                )}
                <p>{item.explicacao}</p>
            </div>
        )
    }

    const itens: ApodItem[] = resultado ? (Array.isArray(resultado) ? resultado : [resultado]) : []

    return (
        <section className='cartão' id='apod'>
            <h2>APOD</h2>
            <p>RESUMO:<br />
                - Astronomy Picture of the Day -APOD-.<br />
                - Um dos sites mais populares da NASA, na verdade, este site é um dos mais populares em todas as agências federais.<br />
                - Tem o apelo popular de um vídeo de Justin Bieber.</p>

            <h3>Modos de pesquisa:</h3>
            <ul>
                <li>
                    <form onSubmit={e => buscar(e, 'data')}>
                        <p><b>Pesquisa por Data</b></p>
                        <hr />
                        <input 
                            type='hidden' 
                            id='apod_modo' 
                            name='apod_modo'
                            value='apod_modo_data' 
                        />
                        <label htmlFor='apod_input_data_unica'>Data*</label>
                        <input
                            type='date'
                            id='apod_input_data_unica'
                            name='apod_input_data_unica'
                            value={dataUnica}
                            onChange={e => setDataUnica(e.target.value)}
                            required
                        />
                        <input type='submit' value='Buscar' />
                    </form>
                </li>

                <li>
                    <form onSubmit={e => buscar(e, 'intervalo')}>
                        <p><b>Pesquisa por Intervalo</b></p>
                        <hr />
                        <input 
                            type='hidden' 
                            id='apod_modo' 
                            name='apod_modo'
                            value='apod_modo_intervalo' 
                        />
                        <label htmlFor='apod_input_data_inicial'>Data Inicial*</label>
                        <input
                            type='date'
                            id='apod_input_data_inicial'
                            name='apod_input_data_inicial'
                            value={dataInicial}
                            onChange={e => setDataInicial(e.target.value)}
                            required
                        />
                        <label htmlFor='apod_input_data_final'>Data Final*</label>
                        <input
                            type='date'
                            id='apod_input_data_final'
                            name='apod_input_data_final'
                            value={dataFinal}
                            onChange={e => setDataFinal(e.target.value)}
                            required
                        />
                        <input type='submit' value='Buscar' />
                    </form>
                </li>

                <li>
                    <form onSubmit={e => buscar(e, 'quantidade')}>
                        <p><b>Pesquisa por Quantidade</b></p>
                        <hr />
                        <input 
                            type='hidden' 
                            id='apod_modo' 
                            name='apod_modo'
                            value='apod_modo_quantidade' 
                        />
                        <label htmlFor='apod_input_quantidade'>Quantidade*</label>
                        <input
                            type='number'
                            id='apod_input_quantidade'
                            name='apod_input_quantidade'
                            placeholder='1'
                            value={quantidade}
                            onChange={e => setQuantidade(Number(e.target.value))}
                            required
                            min={1}
                            max={100}
                            step={1}
                        />
                        <input type='submit' value='Buscar' />
                    </form>
                </li>
            </ul>

            <div id='resposta'>
                {carregando && <p>Carregando...</p>}
                {erro && <p>❌ {erro}</p>}
                {itens.map(item => mostrarResposta(item))}
            </div>
        </section>
    )
}

export default cartao_apod