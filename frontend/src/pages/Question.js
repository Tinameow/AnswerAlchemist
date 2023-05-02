import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Typography, Box, Grid, Divider } from '@mui/material';


function QuestionDetail(props) {
  const { id } = useParams();
  const [question, setQuestion] = useState({});
  const [answers, setAnswers] = useState([]);
  
  // const tags = props.data.tags;
  // const question = props.data.question.title;
  // const answer = props.data.answer;
  // const created = props.data.created;

  function handleClick() {
    window.history.back();
  }

  useEffect(() => {
    // Here you could fetch the question and its answers from an API based on the `id` parameter
    // and set the state accordingly. For example:
    // fetch(`api/questions/${id}`)
    //   .then(response => response.json())
    //   .then(data => {
    //     setQuestion(data.question);
    //     setAnswers(data.answers);
    //   });
    // For this example, we'll just set some dummy data:
    setQuestion({
      title: 'What is the best way to learn React?',
      tags: ['react', 'javascript', 'web-development'],
      created: '2022-05-10 10:30:00',
      content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac metus sed ligula sagittis elementum eget vel augue. Praesent interdum purus nec urna dictum, nec efficitur ipsum finibus. Aliquam in mauris nec quam vehicula malesuada. Etiam blandit ex a turpis malesuada, eget dapibus sapien finibus. Nulla facilisi. Suspendisse potenti. Vestibulum id nibh vel mauris congue dapibus. Quisque eget quam nulla. Vestibulum convallis metus et dolor tristique, quis tempor odio interdum.',
    });
    setAnswers([
      {
        id: 1,
        created: '2022-05-10 11:15:00',
        content: 'There are many great resources to learn React, such as the official documentation, online tutorials, and books. I personally recommend starting with the official tutorial on the React website.',
      },
      {
        id: 2,
        created: '2022-05-10 12:00:00',
        content: 'I agree with the previous answer. Another great way to learn React is to work on projects and practice building real-world applications.',
      },
    ]);
  }, [id]);

  return (
    <>
    Not implemented Yet
    <button onClick={handleClick}>Go back</button>
    </>
    
  );
}

export default QuestionDetail;