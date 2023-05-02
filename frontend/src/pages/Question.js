import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import {
  Box,
  Typography,
  Chip,
  Button
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
  fontSize: '1.2rem',
  marginBottom: '1rem',
});

const Answer = styled(Typography)({
  fontSize: '1.2rem',
  marginBottom: '1rem',
});

const AnswerDate = styled(Typography)({
  color: '#666',
});

function QuestionDetail(props) {
  const { id } = useParams();
  const [question, setQuestion] = useState({});
  const [answers, setAnswers] = useState([]);

  function handleClick() {
    window.history.back();
  }

  useEffect(() => {
    GetQnA(id)
      .then((data) => {
          setQuestion(data.question);
          setAnswers(data.answers);
      })
      .catch((error) => {
          console.error(error);
      })
    
  }, [id]);
  

  return (
    <> 
    { question && 
    (<Box>
      <QuestionWrapper>
        <QuestionTitle variant="h1">{question.title}</QuestionTitle>
        <QuestionDescription>{question.description}</QuestionDescription>
        <TagsWrapper>
          {question.tags?.map((tag) => (
            <Tag key={tag} label={tag} />
          ))}
        </TagsWrapper>
        <Typography variant="subtitle2" align="right">Created: {question.created}</Typography>
      </QuestionWrapper>
      
      { answers?.map((answer, index) => {
          return (
            <AnswerWrapper key={index}>
              <Answer variant="body1">{answer.answer}</Answer>
              <AnswerDate variant="subtitle2" align="right">Created: {answer.created}</AnswerDate>
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