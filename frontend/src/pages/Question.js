import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {
  Box,
  Typography,
  Chip,
  Button,
  Paper
} from '@mui/material';
import { styled } from '@mui/material/styles';

import {GetQnA} from '../api/API';


const TagsWrapper = styled(Box)({
  margin: '0.2rem 1rem',
  display: 'flex',
  flexWrap: 'wrap',
  '& > *': {
    marginRight: '0.5rem',
    marginBottom: '0.5rem',
  },
});

const Tag = styled(Chip)({
  cursor: 'pointer',
});

const QuestionWrapper = styled(Box)({
  margin: '1rem',
  padding: '1rem',
  backgroundColor: '#f0f0f0',
  borderRadius: '0.5rem',
});

const AnswerWrapper = styled(Box)({
  margin: '1rem',
  padding: '1rem',
  backgroundColor: '#f8f8f8',
  borderRadius: '0.5rem',
});

const QuestionTitle = styled(Typography)({
  fontWeight: 'bold',
  fontSize: '1.5rem',
  marginBottom: '1rem',
});

const QuestionDescription = styled(Typography)({
  fontSize: '1rem',
  marginBottom: '1rem',
});

const Answer = styled(Typography)({
  fontSize: '1rem',
  marginBottom: '1rem',
});

const AnswerDate = styled(Typography)({
  color: '#666',
});

function QuestionDetail(props) {
  const { id } = useParams();
  const [question, setQuestion] = useState({});
  const [answers, setAnswers] = useState([]);
  const [summary, setSummary] = useState("");
  const navigate = useNavigate();

  function handleClick() {
    navigate(-1);
  }

  useEffect(() => {
    GetQnA(id)
      .then((data) => {
          setQuestion(data.question);
          setAnswers(data.answers);
          setSummary(data.summary);
      })
      .catch((error) => {
          console.error(error);
      })
    
  }, [id]);
  

  return (
    <> 
    { question && 
    (<Box sx={{m: 2}}>
      <QuestionWrapper>
        <QuestionTitle variant="h1">{question.title}</QuestionTitle>
        <QuestionDescription>
          <div dangerouslySetInnerHTML={{ __html: question.description }} />
        </QuestionDescription>
        <TagsWrapper>
          {question.tags?.map((tag) => (
            <Tag key={tag} label={tag} />
          ))}
        </TagsWrapper>
        <Typography variant="subtitle2" align="right">Created: {question.created}</Typography>
      </QuestionWrapper>

      {summary && 
          <AnswerWrapper>
            <Typography variant="h5" sx={{mb:3}}>
              Answer Summary
            </Typography>
            <Typography variant="body1">
              <div dangerouslySetInnerHTML={{ __html: summary }} />
            </Typography>
          </AnswerWrapper> 
        }
      
      { answers?.map((answer, index) => {
          return (
            <AnswerWrapper key={index}>
              <Typography variant="h6" sx={{mb:3}}>
              Answer {index+1}
              </Typography>
              <Answer variant="body1"><div dangerouslySetInnerHTML={{ __html: answer.answer }} /></Answer>
              {/* <AnswerDate variant="subtitle2" align="right">Created: {answer.created}</AnswerDate> */}
            </AnswerWrapper>
      )})
      }
    </Box>)}
    <Box display="flex" justifyContent="center">
      <Button variant="outlined" onClick={handleClick} color="primary">Go back</Button>
    </Box>
    </>
  );
}

export default QuestionDetail;