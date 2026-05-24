export class NasaApi {

     constructor() {

        this.base_url = "http://127.0.0.1:3000";
    }

    async search_date(date) {
        try {
            console.log(date);

            const answer = await fetch(
                `${this.base_url}/nasa/apod/photo?date=${date}`
            );

            const data = await answer.json();

            console.log("dados da chamada rest search_result_apod:", data);

            return data;

        } catch (erro) {

            console.log("Erro:", erro);

        }

    }

    async search_date_interval(initial_date, end_date) {
         try { 
            console.log(initial_date, end_date);

            const answer = await fetch(
                `${this.base_url}/nasa/apod/photos/interval?start_date=${initial_date}&end_date=${end_date}`
            );

            const data = await answer.json();

            console.log("dados da chamada rest search_result_interval:", data);

            return data;

        } catch (erro) {
            console.log("Erro:", erro);
        }
    }

    async search_count(count){
         try { 
            console.log(count);

            const answer = await fetch(
                `${this.base_url}/nasa/apod/photos/count?count=${count}`
            );

            const data = await answer.json();

            console.log("dados da chamada rest search_count:", data);

            return data;

        } catch (erro) {
            console.log("Erro:", erro);
        }
    }

    async search_thumbs(thumbs){
            try {
                console.log(thumbs);

                const answer = await fetch(
                    `${this.base_url}/nasa/apod/photos/thumbs?thumbs=${thumbs}`
                );

                const data = await answer.json();

                console.log("dados da chamada rest search_thumbs:", data);  

                return data;
                
            } catch (erro) {
                console.log("Erro:", erro);
            }
    }
        
}

