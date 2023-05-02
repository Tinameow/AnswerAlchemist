import React from 'react';
import { styled, alpha } from '@mui/material/styles';
import {
  Card,
  CardContent,
  Typography,
  Chip,
  Stack
} from '@mui/material';

const StyledCard = styled(Card)({
  marginBottom: '1rem',
  backgroundColor: '#f7f7f7',
  width: '100%',
});

const StyledCardContent = styled(CardContent)({
  padding: '1rem',
});

const QuestionTitle = styled(Typography)({
  fontSize: '1.2rem',
  fontWeight: 'bold',
  marginTop: '0.2rem',
  marginLeft: '1rem',
});

const AnswerText = styled(Typography)({
  fontSize: '1rem',
  marginBottom: '0.5rem',
});

const TagsWrapper = styled('div')({
  margin: '0.2rem 1rem',
  display: 'flex',
  flexWrap: 'wrap',
  paddingRight: '1rem',
  '& > *': {
    marginRight: '0.5rem',
    marginBottom: '0.5rem',
  },
});

const StyledChip = styled(Chip)({
  backgroundColor: alpha('#0066cc', 0.1),
  color: '#0066cc',
  '&:hover': {
    backgroundColor: alpha('#0066cc', 0.2),
  },
});

function QnAItem(props) {
  const tags = props.data.tags;
  const question = props.data.question.title;
  const answer = props.data.answer;
  const created = new Date(props.data.created);

  return (
    <StyledCard>
      <StyledCardContent>
        <AnswerText>
          <div dangerouslySetInnerHTML={{ __html: answer }} />     
        </AnswerText>
      </StyledCardContent>

      <QuestionTitle>{question}</QuestionTitle>
    
      <Stack
        direction="row"
        justifyContent="space-between"
        alignItems="baseline"
        spacing={2}
      >
        {tags && (
          <TagsWrapper>
            {tags.map((tag) => (
              <StyledChip key={tag} label={tag} />
            ))}
          </TagsWrapper>
        )}
        <TagsWrapper>
          <Typography variant="caption">Created: {created.toLocaleString()}</Typography>
        </TagsWrapper>
      </Stack>
      
    </StyledCard>
  );
}

export default QnAItem;