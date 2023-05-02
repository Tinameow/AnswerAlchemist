import {useState} from 'react';
import {Link} from "react-router-dom";
import {Box, Stack} from '@mui/material';
import SearchBar from '../components/SearchBar';
import QnAItem from '../components/QnAItem';
import {GetQnAList} from '../api/API';
import {mock_data} from '../api/MockData';


function Search (props) {
    const [searchInput, setSearchInput] = useState("");
    const [results, setResults] = useState(mock_data);

    const handleInputChange = (e) => {
        e.preventDefault();
        setSearchInput(e.target.value);
        setResults(mock_data);
        // GetQnAList(e.target.value)
        //     .then((result) => {
        //         setResults(result);
        //     })
        //     .catch((error) => {
        //         console.error(error);
        //     })
    };
    
    return (
        <>
        <Stack spacing={2} sx={{mt:5}} alignItems='center'>
            <Box sx={{ width: {xs: 400, sm: 600, md: 700, lg: 700} }}>
                <SearchBar onChange={handleInputChange} />
            </Box>
        </Stack>

        {!results ? false:
        <Box sx={{ width: {xs: 600, sm: 700, md: 800, lg: 900, xl:1000}, margin:'auto'}}>
            <Stack alignItems='strench' spacing={2} sx={{mt:5}}>
                {results.map((item)=>{return (
                    <Link style={{textDecoration:'none',color:'white'}} key={item.id} id={item.id} data={item} to={`../question/${item.id}`}>
                        <QnAItem key={item.id} id={item.id} data={item} />
                    </Link>
                )})}
            </Stack>
        </Box>
        }

        </>
    );
}

export default Search;