import './App.css';
import { HashRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import NoMatch from './pages/NoMatch';
import Search from "./pages/Search";
import Question from "./pages/Question";
import { AppBar, Toolbar, Typography, Box } from '@mui/material';

function Footer() {
  return (
    <AppBar position="static" color="primary">
      <Toolbar>
        <Box flexGrow={1}>
          <Typography variant="body1" color="inherit">
            Copyright © {new Date().getFullYear()}
          </Typography>
        </Box>
        <Typography variant="body1" color="inherit">
          My App
        </Typography>
      </Toolbar>
    </AppBar>
  );
}

function App() {
  return (
    <HashRouter basename={process.env.PUBLIC_URL}>
      <Routes>
        <Route path="/search" element={<Search />} />
        <Route path="/question/:id" element={<Question />} />
        <Route path="*" element={<NoMatch />} />
      </Routes>
      {/* <Footer />    */}
    </HashRouter>
  );
}

export default App;
