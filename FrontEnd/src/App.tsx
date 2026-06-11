
import './App.css'
import Cartao_neo from './cartoes/cartao_neo'
import Cartao_apod from './cartoes/cartao_apod'
import Cartao_donki from './cartoes/cartao_donki'
import Cartao_epic from './cartoes/cartao_epic';
import Cartao_insight from './cartoes/cartao_insight';
import Cartao_image_and_video_library from './cartoes/cartao_image_and_video_library';

function App() {

  return (
    <>

      <div className='separacao'></div>

      <Cartao_apod></Cartao_apod>

      <div className='separacao'></div>
      
      <Cartao_neo></Cartao_neo>

      <div className='separacao'></div>

      <Cartao_donki></Cartao_donki>

      <div className='separacao'></div>

      <Cartao_epic></Cartao_epic>

      <div className='separacao'></div>

      <Cartao_insight></Cartao_insight>

      <div className='separacao'></div>

      <Cartao_image_and_video_library></Cartao_image_and_video_library>

      <div className='separacao'></div>

    </>
  )
}

export default App
