import {useState} from 'react';
import {Link} from "react-router-dom";
import {Box, Stack, ToggleButton, ToggleButtonGroup} from '@mui/material';



function Search (props) {
    const [results, setResults] = useState([]);

    const handleInputChange = (event) => {
        event.preventDefault();
    }


    return (
        <div>
            search page
        </div>
    );
}

export default Search;