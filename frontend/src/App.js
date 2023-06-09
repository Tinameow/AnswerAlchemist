import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import NoMatch from './pages/NoMatch';
import Search from "./pages/Search";
import QuestionDetail from "./pages/Question";
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
    <BrowserRouter basename={process.env.PUBLIC_URL}>
      <Routes>
        <Route path="/search" element={<Search />} />
        <Route path="/question/:id" element={<QuestionDetail />} />
        <Route path="*" element={<NoMatch />} />
      </Routes>
      {/* <Footer />    */}
    </BrowserRouter>
  );
}

export default App;
