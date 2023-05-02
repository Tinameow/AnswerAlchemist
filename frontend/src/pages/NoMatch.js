import { Link } from "react-router-dom";

function NoMatch() {
  return (
    <div>
      <h2>Nothing to see here!</h2>
      <p>
        <Link to="/search">Go to the search page</Link>
      </p>
    </div>
  );
}

export default NoMatch;