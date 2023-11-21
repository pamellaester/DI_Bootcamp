import React, { createContext, useContext, useState } from "react";

export const ThemeContext = createContext(null);

function ThemeProvider({ children }) {
    const[theme, setTheme] = useState("Dark Mode")
    
    const toggleTheme = () => {
        setTheme((current) => (current === "light" ? "dark": "light"))
      }

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error("useTheme must be used within a ThemeProvider");
  }
  return context;
}

export { ThemeProvider, useTheme };