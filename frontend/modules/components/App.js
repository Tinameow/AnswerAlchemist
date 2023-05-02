// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
	// usestate for setting a javascript
	// object for storing and using data
	const [data, setdata] = useState({
		title: "",
		answer: ""
	});

	// Using useEffect for single rendering
	useEffect(() => {
		// Using fetch to fetch the api from
		// flask server it will be redirected to proxy
		fetch("/filter").then((res) =>
        res.json().then((data) => {
            // Setting the list of items from api
            const items = data.items.map((item) => ({
                title: item.title,
                answer: item.answer,
                // tags: item.tags
            }));
            setItems(items);
        })
    );
	}, []);

	// return (
	// 	<div className="App">
	// 		<header className="App-header">
	// 			<h1>React and flask</h1>
	// 			{/* Calling a data from setdata for showing */}
	// 			<p>{data.name}</p>
	// 			<p>{data.age}</p>
	// 			<p>{data.date}</p>
	// 			<p>{data.programming}</p>

	// 		</header>
	// 	</div>
	// );
}

export default App;
