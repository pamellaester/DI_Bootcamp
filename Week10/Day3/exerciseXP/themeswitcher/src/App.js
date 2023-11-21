import "./App.css"
import ReactSwitch from "react-switch";
import { ThemeProvider, useTheme } from "./themeSwitcher";

function ThemeSwitcher() {
  const { theme, toggleTheme } = useTheme();

  return (
    <div className="App" id={theme}>
      <h1>THEME SWITCHER</h1>
      <label>{theme === "light" ? "Light Mode": "Dark Mode" }</label>
      <ReactSwitch onChange={toggleTheme} checked={theme === "dark"} />
    </div>
  );
}

function App() {

  return (
    <ThemeProvider>
      <div>
        <ThemeSwitcher />
      </div>
    </ThemeProvider>
  );
}

export default App;
