import { useState } from 'react'

type Modo = 'insight'

function cartao_insight() {
    const [resultado, setResultado] = useState<any>(null)
    const [erro, setErro] = useState<string | null>(null)
    const [carregando, setCarregando] = useState(false)

    const BASE_URL = 'http://localhost:3000/nasa'

    const urls: Record<Modo, string> = {
        insight: `${BASE_URL}/insight`,
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
        <section className='cartão' id='insight'>
            <h2>InSight</h2>
            <p>RESUMO:<br />
                - Mars Weather Service API.<br />
                - Retorna dados meteorológicos dos últimos sete dias de Marte coletados pela sonda InSight da NASA.
            </p>

            <h3>Modos de pesquisa:</h3>
            <ul>
                <li>
                    <form onSubmit={e => buscar(e, 'insight')}>
                        <p><b>Clima recente em Marte</b></p>
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

export default cartao_insight