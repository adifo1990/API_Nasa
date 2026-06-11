import { useState } from 'react'

type Modo = 'cme' | 'cmeanalysis' | 'gst' | 'ips' | 'flr' | 'sep' | 'mpc' | 'rbe' | 'hss' | 'wsaenlilsimulation' | 'notifications'

function cartao_donki() {
    const [dataInicial, setDataInicial] = useState('')
    const [dataFinal, setDataFinal] = useState('')
    const [tipo, setTipo] = useState('')

    const [resultado, setResultado] = useState<any>(null)
    const [erro, setErro] = useState<string | null>(null)
    const [carregando, setCarregando] = useState(false)

    const BASE_URL = 'http://localhost:3000/nasa'

    const urls: Record<Modo, string> = {
        cme:                 `${BASE_URL}/donki/cme?start_date=${dataInicial}&end_date=${dataFinal}`,
        cmeanalysis:         `${BASE_URL}/donki/cmeanalysis?start_date=${dataInicial}&end_date=${dataFinal}`,
        gst:                 `${BASE_URL}/donki/gst?start_date=${dataInicial}&end_date=${dataFinal}`,
        ips:                 `${BASE_URL}/donki/ips?start_date=${dataInicial}&end_date=${dataFinal}`,
        flr:                 `${BASE_URL}/donki/flr?start_date=${dataInicial}&end_date=${dataFinal}`,
        sep:                 `${BASE_URL}/donki/sep?start_date=${dataInicial}&end_date=${dataFinal}`,
        mpc:                 `${BASE_URL}/donki/mpc?start_date=${dataInicial}&end_date=${dataFinal}`,
        rbe:                 `${BASE_URL}/donki/rbe?start_date=${dataInicial}&end_date=${dataFinal}`,
        hss:                 `${BASE_URL}/donki/hss?start_date=${dataInicial}&end_date=${dataFinal}`,
        wsaenlilsimulation:  `${BASE_URL}/donki/wsaenlilsimulation?start_date=${dataInicial}&end_date=${dataFinal}`,
        notifications:`${BASE_URL}/donki/notifications?start_date=${dataInicial}&end_date=${dataFinal}&type=${tipo}`,
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

    const cartaoInput = (tipoUrl: string, modo: Modo, textoP: string) => (
        <li>
            <form onSubmit={e => buscar(e, modo)}>
                <p><b>{textoP}</b></p>
                <hr />
                <label htmlFor={`${tipoUrl}_data_inicial`}>Data Inicial*</label>
                <input
                    type='date'
                    id={`${tipoUrl}_data_inicial`}
                    name={`${tipoUrl}_data_inicial`}
                    value={dataInicial}
                    onChange={e => setDataInicial(e.target.value)}
                    required
                />
                <label htmlFor={`${tipoUrl}_data_final`}>Data Final*</label>
                <input
                    type='date'
                    id={`${tipoUrl}_data_final`}
                    name={`${tipoUrl}_data_final`}
                    value={dataFinal}
                    onChange={e => setDataFinal(e.target.value)}
                    required
                />
                <input type='submit' value='Buscar' />
            </form>
        </li>
    )

    return (
        <section className='cartão' id='donki'>
            <h2>Asteroids - DONKI</h2>
            <p>RESUMO:<br />
                - Space Weather Database Of Notifications, Knowledge, Information -DONKI-.<br />
                - Base de dados de clima espacial com notificações e análises de eventos solares.
            </p>

            <h3>Modos de pesquisa:</h3>
            <ul>
                {cartaoInput('donki_cme', 'cme', 'CME - Ejeção de Massa Coronal')}

                {cartaoInput('donki_cmeanalysis', 'cmeanalysis', 'CME Analysis')}

                {cartaoInput('donki_gst', 'gst', 'GST - Tempestade Geomagnética')}

                {cartaoInput('donki_ips', 'ips', 'IPS - Choque Interplanetário')}
                
                {cartaoInput('donki_flr', 'flr', 'FLR - Flare Solar')}

                {cartaoInput('donki_sep', 'sep', 'SEP - Partícula Energética Solar')}

                {cartaoInput('donki_mpc', 'mpc', 'MPC - Corrente de Plasma Magnetopause')}

                {cartaoInput('donki_rbe', 'rbe', 'RBE - Cinturão de Radiação')}

                {cartaoInput('donki_hss', 'hss', 'HSS - Fluxo de Alta Velocidade')}

                {cartaoInput('donki_wsa', 'wsaenlilsimulation', 'WSA + Enlil Simulation')}

                <li>
                    <form onSubmit={e => buscar(e, 'notifications')}>
                        <p><b>Notificações</b></p>
                        <hr />
                        <label htmlFor='donki_notif_ata_inicial'>Data Inicial*</label>
                        <input
                            type='date'
                            id='donki_notif_data_inicial'
                            name='donki_notif_data_inicial'
                            value={dataInicial}
                            onChange={e => setDataInicial(e.target.value)}
                            required
                        />
                        <label htmlFor='donki_notif_data_final'>Data Final*</label>
                        <input
                            type='date'
                            id='donki_notif_data_final'
                            name='donki_notif_data_final'
                            value={dataFinal}
                            onChange={e => setDataFinal(e.target.value)}
                            required
                        />
                        <label htmlFor='donki_input_tipo'>Tipo*</label>
                        <select
                            id='donki_input_tipo'
                            name='donki_input_tipo'
                            value={tipo}
                            onChange={e => setTipo(e.target.value)}
                            required
                        >
                            <option disabled value=''>selecione o tipo</option>
                            <option value='all'>all</option>
                            <option value='FLR'>FLR</option>
                            <option value='SEP'>SEP</option>
                            <option value='CME'>CME</option>
                            <option value='IPS'>IPS</option>
                            <option value='MPC'>MPC</option>
                            <option value='GST'>GST</option>
                            <option value='RBE'>RBE</option>
                            <option value='report'>report</option>
                        </select>
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

export default cartao_donki