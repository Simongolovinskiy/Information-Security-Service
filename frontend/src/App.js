import './App.css';
import Footer from './components/footer/Footer';
import Header from './components/header/Header';
import Hero from './components/hero/Hero';
import Result from './components/result/Result';

function App() {
  return (
    <div className="App">
      <Header />
      <Hero />
      <Result />
      <Footer />
    </div>
  );
}

export default App;
