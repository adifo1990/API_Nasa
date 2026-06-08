function cartao_apod() {

    return(
        <section className='cartão' id='apod'>
            <h2>APOD</h2>
            <p>RESUMO:<br/>
                - Astronomy Picture of the Day -APOD-.<br/>
                - Um dos sites mais populares da NASA, na verdade, este site é um dos mais populares em todas as agências federais.<br/>
                - Tem o apelo popular de um vídeo de Justin Bieber.</p>
            
            <h3>Modos de pesquisa:</h3>
            <ul>
                <li>
                    <form>
                        <input type='hidden' id='apod_radio_data' value='apod_data' name='modo_apod' />
                        <p><b>Pesquisa por Data</b></p>
                        <hr />
                        <label htmlFor='apod_input_data_unica'>Data*</label>
                        <input type='date' id='apod_input_data_unica' required />

                        <input type='submit' value='Buscar' />
                    </form>
                </li>

                <li>
                    <form>
                        <input type='hidden' id='apod_radio_intrevalo' value='apod_intervalo' name='modo_apod' />
                        <p><b>Pesquisa por Intervalo</b></p>
                        <p></p>
                        <hr />
                        <label htmlFor='apod_input_data_inicial'>Data Incial*</label>
                        <input type='date' id='apod_input_data_inicial' required />

                        <label htmlFor="apod_input_data_final">Data Final*</label>
                        <input type='date' id='apod_input_data_final' required />

                        <input type='submit' value='Buscar' />
                    </form>
                </li>

                <li>
                    <form>
                        <input type='hidden' id='apod_radio_quantidade' value='apod_quantidade' name='modo_apod' />
                        <p><b>Pesquisa por Quantidade</b></p>
                        <hr />
                        <label htmlFor='apod_input_quantidade'>Quantidade*</label>
                        <input type='number' id='apod_input_quantidade' placeholder='1' required min={1} max={10} step={1} />

                        <input type='submit' value='Buscar' />
                    </form>
                </li>

                <li>
                    <form>
                        <input type='hidden' id='apod_radio_url' value='apod_url' name='modo_apod' />
                        <p><b>Pesquisa por URL</b></p>
                        <hr />
                        <label htmlFor='apod_input_url'>URL*</label>
                        <input type='url' id='apod_input_url' placeholder='https://...' required />
        
                        <input type='submit' value='Buscar' />
                    </form>
                </li>
            </ul>
            <div id='resposta'>

            </div>
        </section>
    )
}
export default cartao_apod