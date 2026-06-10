function cartao_neo() {

    return(
        <section className='cartão' id="neo">
            <h2>Asteroids - NeoWs</h2>
            <p>RESUMO:<br/>
                - Near Earth Object Web Service -NeoWs-.<br/>
                - Um serviço web RESTful para informações sobre asteroides próximos à Terra.
            </p>
            
            <h3>Modos de pesquisa:</h3>
            <ul>
                <li>
                    <form>
                        <input 
                            type='hidden' 
                            id='neo_modo' 
                            name='neo_modo'
                            value='neo_intervalo' 
                        />
                        <p><b>Pesquisa por Intervalo</b></p>
                        <hr />
                        <label htmlFor='neo_input_data_inicial'>Data Incial*</label>
                        <input 
                            type='date' 
                            id='neo_input_data_inicial' 
                            name='neo_input_data_inicial'
                            required 
                        />

                        <label htmlFor="neo_input_data_final">Data Final*</label>
                        <input 
                            type='date' 
                            id='neo_input_data_final'
                            name='neo_input_data_final'
                            required 
                        />

                        <input type='submit' value='Buscar' />
                    </form>
                </li>

                <li>
                    <form>
                        <input 
                            type='hidden' 
                            id='neo_modo' 
                            name='neo_modo' 
                            value='neo_id' 
                        />
                        <p><b>Pesquisa por ID</b></p>
                        <hr />
                        <label htmlFor='neo_input_id'>ID*</label>
                        <input 
                            type='text' 
                            id='neo_input_id' 
                            name='neo_input_id' 
                            inputMode='numeric' 
                            placeholder='2001620' 
                            pattern="[0-9]{1,7}" 
                            maxLength={7} 
                            required 
                        />

                        <input type='submit' value='Buscar' />
                    </form>
                </li>

                <li>
                    <form>
                        <input 
                            type='hidden' 
                            id='neo_modo' 
                            name='neo_modo'  
                            value='neo_browse'  
                        />
                        <p><b>listar todos</b></p>
                        <hr />
                        <input type='submit' value='Buscar' />
                    </form>
                </li>
            </ul>
            <div id='resposta'>

            </div>
        </section>
    )
}
export default cartao_neo