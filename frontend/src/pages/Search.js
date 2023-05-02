import {useEffect, useState} from 'react';
import {Link} from "react-router-dom";
import {Box, Stack, Chip} from '@mui/material';
import SearchBar from '../components/SearchBar';
import QnAItem from '../components/QnAItem';
import {GetQnAList} from '../api/API';
import {mock_results, mock_tags} from '../api/MockData';


function Search(props) {
    const [searchInput, setSearchInput] = useState("");
    const [results, setResults] = useState(mock_results);
    const [tags, setTags] = useState(mock_tags);
    const [chosenTags, setChosenTags] = useState(["Python"]);
  
    const handleInputChange = (e) => {
      e.preventDefault();
      setSearchInput(e.target.value);
      setResults(mock_results);
  
      // GetQnAList(e.target.value)
      //     .then((result) => {
      //         setResults(result.results);
      //         setTags(results.tags);
      //     })
      //     .catch((error) => {
      //         console.error(error);
      //     })
    };
  
    const handleTagFilter = (tag) => {
      if (chosenTags.includes(tag)) {
        setChosenTags(chosenTags.filter((t) => t !== tag));
      } else {
        setChosenTags([...chosenTags, tag]);
      }
    };
  
    const filteredResults = results.filter((item) => {
      return chosenTags.every((tag) => item.tags.includes(tag));
    });

  
    return (
      <>
        <Stack spacing={2} sx={{ mt: 5 }} alignItems="center">
          <Box sx={{ width: { xs: 400, sm: 600, md: 700, lg: 700 } }}>
            <SearchBar onChange={handleInputChange} />
          </Box>
          <Box>
            {tags.map((tag) => (
              <Chip
                key={tag}
                label={tag}
                onClick={() => handleTagFilter(tag)}
                sx={{
                  mr: 1,
                  mb: 1,
                  backgroundColor: chosenTags.includes(tag)
                    ? "#9e9e9e"
                    : "#e0e0e0",
                }}
              />
            ))}
          </Box>
        </Stack>
  
        {!filteredResults ? false : (
          <Box sx={{ width: { xs: 600, sm: 700, md: 800, lg: 900, xl: 1000 }, margin: "auto" }}>
            <Stack alignItems="stretch" spacing={2} sx={{ mt: 5 }}>
              {filteredResults.map((item) => {
                return (
                  <Link
                    style={{ textDecoration: "none", color: "white" }}
                    key={item.id}
                    id={item.id}
                    data={item}
                    to={`../question/${item.id}`}
                  >
                    <QnAItem key={item.id} id={item.id} data={item} />
                  </Link>
                );
              })}
            </Stack>
          </Box>
        )}
      </>
    );
  }
  

export default Search;