import { useState } from 'react'

type Modo =
    | 'natural' | 'natural_date' | 'natural_all' | 'natural_available'
    | 'enhanced' | 'enhanced_date' | 'enhanced_all' | 'enhanced_available'
    | 'aerosol' | 'aerosol_date' | 'aerosol_all' | 'aerosol_available'
    | 'cloud' | 'cloud_date' | 'cloud_all' | 'cloud_available'

function cartao_epic() {
    const [data, setData] = useState('')

    const [resultado, setResultado] = useState<any>(null)
    const [erro, setErro] = useState<string | null>(null)
    const [carregando, setCarregando] = useState(false)

    const BASE_URL = 'http://localhost:3000/nasa'

    const urls: Record<Modo, string> = {
        natural:             `${BASE_URL}/epic/natural`,
        natural_date:        `${BASE_URL}/epic/natural/date/${data}`,
        natural_all:         `${BASE_URL}/epic/natural/all/`,
        natural_available:   `${BASE_URL}/epic/natural/available`,
        enhanced:            `${BASE_URL}/epic/enhanced`,
        enhanced_date:       `${BASE_URL}/epic/enhanced/date/${data}`,
        enhanced_all:        `${BASE_URL}/epic/enhanced/all/`,
        enhanced_available:  `${BASE_URL}/epic/enhanced/available`,
        aerosol:             `${BASE_URL}/epic/aerosol`,
        aerosol_date:        `${BASE_URL}/epic/aerosol/date/${data}`,
        aerosol_all:         `${BASE_URL}/epic/aerosol/all/`,
        aerosol_available:   `${BASE_URL}/epic/aerosol/available`,
        cloud:               `${BASE_URL}/epic/cloud`,
        cloud_date:          `${BASE_URL}/epic/cloud/date/${data}`,
        cloud_all:           `${BASE_URL}/epic/cloud/all/`,
        cloud_available:     `${BASE_URL}/epic/cloud/available`,
    }

    async function buscar(e: React.FormEvent, modo: Modo) {
        e.preventDefault()
        setErro(null)
        setResultado(null)
        setCarregando(true)
        try {
            const res = await fetch(urls[modo])
            const dados = await res.json()
            if (dados.error) throw new Error(dados.error)
            setResultado(dados)
        } catch (err: any) {
            setErro(err.message || 'Erro ao buscar')
        } finally {
            setCarregando(false)
        }
    }

    const cartoesInput = (tipoUrl: string, modo: Modo, textoP: string) => (
        <>
            <li>
                <form onSubmit={e => buscar(e, modo)}>
                    <p><b>{textoP} - Mais recente</b></p>
                    <hr />
                    <input type='submit' value='Buscar' />
                </form>
            </li>

            <li>
                <form onSubmit={e => buscar(e, `${modo}_date` as Modo)}>
                    <p><b>{textoP} - Por Data</b></p>
                    <hr />
                    <label htmlFor={`${tipoUrl}_data`}>Data*</label>
                    <input
                        type='date'
                        id={`${tipoUrl}_data`}
                        name={`${tipoUrl}_data`}
                        value={data}
                        onChange={e => setData(e.target.value)}
                        required
                    />
                    <input type='submit' value='Buscar' />
                </form>
            </li>

            <li>
                <form onSubmit={e => buscar(e, `${modo}_all` as Modo)}>
                    <p><b>{textoP} - Todos</b></p>
                    <hr />
                    <input type='submit' value='Buscar' />
                </form>
            </li>

            <li>
                <form onSubmit={e => buscar(e, `${modo}_available` as Modo)}>
                    <p><b>{textoP} - Disponíveis</b></p>
                    <hr />
                    <input type='submit' value='Buscar' />
                </form>
            </li>
        </>
    )

    return (
        <section className='cartão' id='epic'>
            <h2>EPIC</h2>
            <p>RESUMO:<br />
                - Eimagens diárias coletadas pelo instrumento Earth Polychromatic Imaging Camera -EPIC- da DSCOVR.<br />
                - O desenvolvimento da API EPIC começou em 2015 e é apoiado pela equipe de desenvolvimento web do Laboratório de Atmosferas da Divisão de Ciências da Terra do Goddard Space Flight Center
            </p>

            <h3>Modos de pesquisa:</h3>
            <ul>
                {cartoesInput('epic_natural', 'natural', 'natural')}
                {cartoesInput('epic_enhanced', 'enhanced', 'enhanced')}
                {cartoesInput('epic_aerosol', 'aerosol', 'aerosol')}
                {cartoesInput('epic_cloud', 'cloud', 'cloud')}
            </ul>

            <div id='resposta'>
                {carregando && <p>Carregando...</p>}
                {erro && <p>❌ {erro}</p>}
                {resultado && <pre>{JSON.stringify(resultado, null, 2)}</pre>}
            </div>
        </section>
    )
}

export default cartao_epic