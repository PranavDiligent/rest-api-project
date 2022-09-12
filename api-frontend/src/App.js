import logo from './logo.svg';
import './App.css';
import Hello from './components/Hello';
import FuncComponent from './components/Hello';
import MyClass from './components/MyClass';

function App() {
  return (
    <div className="App">
      <div className="App-header">
        <h1>HELLO FROM PRANAV</h1>
      {/* <Hello></Hello> */}
      <FuncComponent name="try"></FuncComponent>
      <MyClass email="this is class property"></MyClass>
      
      </div>
    </div>
  );
}

export default App;
