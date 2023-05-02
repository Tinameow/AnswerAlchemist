import { Link } from "react-router-dom";

function Question(props) {
  // const tags = props.data.tags;
  // const question = props.data.question.title;
  // const answer = props.data.answer;
  // const created = props.data.created;

  function handleClick() {
    window.history.back();
  }

  return (
    <button onClick={handleClick}>Go back</button>
  );
}

export default Question;