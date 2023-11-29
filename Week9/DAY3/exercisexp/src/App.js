import logo from './logo.svg';
import './App.css';
import UserFavoriteAnimals from './UserFavoriteAnimals';
import Exercise from './Exercise3';

function App() {
  const myelement = <h1>I Love JSX!</h1>;
  const sum = 5 + 5;
  const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals : ['Horse','Turtle','Elephant','Monkey']
  }; 
  return (
    <div className="App">
      <header className="App-header">
        {myelement}
        <h1>React is {sum} times better with JSX</h1>
        <p>hello world!</p>
        <h3>first name: {user.firstName}</h3>
        <h3>last name: {user.lastName}</h3>
        <UserFavoriteAnimals animals={user.favAnimals} />
        <Exercise />
      </header>
    </div>
  );
}

export default App;
