import { useState } from 'react'

type Modo = 'search' | 'asset' | 'metadata' | 'captions'

function cartao_image_and_video_library() {
    const [q, setQ] = useState('')
    const [mediaType, setMediaType] = useState('')
    const [yearStart, setYearStart] = useState('')
    const [yearEnd, setYearEnd] = useState('')
    const [nasaId, setNasaId] = useState('')

    const [resultado, setResultado] = useState<any>(null)
    const [erro, setErro] = useState<string | null>(null)
    const [carregando, setCarregando] = useState(false)

    const BASE_URL = 'http://localhost:3000/nasa'

    const urls: Record<Modo, string> = {
        search:   `${BASE_URL}/image_and_video_library/search?q=${q}&media_type=${mediaType}&year_start=${yearStart}&year_end=${yearEnd}`,
        asset:    `${BASE_URL}/image_and_video_library/asset/${nasaId}`,
        metadata: `${BASE_URL}/image_and_video_library/metadata/${nasaId}`,
        captions: `${BASE_URL}/image_and_video_library/captions/${nasaId}`,
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

    const campoNasaId = (prefixo: string) => (
        <>
            <label htmlFor={`${prefixo}_nasa_id`}>NASA ID*</label>
            <input
                type='text'
                id={`${prefixo}_nasa_id`}
                name={`${prefixo}_nasa_id`}
                placeholder='PIA12235'
                value={nasaId}
                onChange={e => setNasaId(e.target.value)}
                required
            />
        </>
    )

    return (
        <section className='cartão' id='image_and_video_library'>
            <h2>Image and Video Library</h2>
            <p>RESUMO:<br />
                - NASA Image and Video Library.<br />
                - Acesso ao catálogo de imagens, vídeos e áudios da NASA.
            </p>

            <h3>Modos de pesquisa:</h3>
            <ul>
                <li>
                    <form onSubmit={e => buscar(e, 'search')}>
                        <p><b>Pesquisa por Termo</b></p>
                        <hr />
                        <label htmlFor='library_input_q'>Termo*</label>
                        <input
                            type='text'
                            id='library_input_q'
                            name='library_input_q'
                            placeholder='apollo'
                            value={q}
                            onChange={e => setQ(e.target.value)}
                            required
                        />
                        <label htmlFor='library_input_media_type'>Tipo de mídia</label>
                        <select
                            id='library_input_media_type'
                            name='library_input_media_type'
                            value={mediaType}
                            onChange={e => setMediaType(e.target.value)}
                        >
                            <option value=''>todos</option>
                            <option value='image'>image</option>
                            <option value='video'>video</option>
                            <option value='audio'>audio</option>
                        </select>
                        <label htmlFor='library_input_year_start'>Ano inicial</label>
                        <input
                            type='number'
                            id='library_input_year_start'
                            name='library_input_year_start'
                            placeholder='1960'
                            min={1920}
                            max={2100}
                            value={yearStart}
                            onChange={e => setYearStart(e.target.value)}
                        />
                        <label htmlFor='library_input_year_end'>Ano final</label>
                        <input
                            type='number'
                            id='library_input_year_end'
                            name='library_input_year_end'
                            placeholder='2024'
                            min={1920}
                            max={2100}
                            value={yearEnd}
                            onChange={e => setYearEnd(e.target.value)}
                        />
                        <input type='submit' value='Buscar' />
                    </form>
                </li>

                <li>
                    <form onSubmit={e => buscar(e, 'asset')}>
                        <p><b>Asset por NASA ID</b></p>
                        <hr />
                        {campoNasaId('library_asset')}
                        <input type='submit' value='Buscar' />
                    </form>
                </li>

                <li>
                    <form onSubmit={e => buscar(e, 'metadata')}>
                        <p><b>Metadata por NASA ID</b></p>
                        <hr />
                        {campoNasaId('library_metadata')}
                        <input type='submit' value='Buscar' />
                    </form>
                </li>

                <li>
                    <form onSubmit={e => buscar(e, 'captions')}>
                        <p><b>Captions por NASA ID</b></p>
                        <hr />
                        {campoNasaId('library_captions')}
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

export default cartao_image_and_video_library