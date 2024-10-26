import React, { useEffect, useState } from 'react';
import './App.css';

type Paper = {
  id: number;
  title: string;
  url: string;
  abstract: string;
}

function App() {

  const [papers, setPapers] = useState<Paper[]>([]);

  useEffect(() => {
    fetch('http://localhost:8000/papers')
      .then(response => response.json())
      .then(data => {
        setPapers(data.papers);
      });
  }, []);

  return (
    <main>
      <h1>Papers</h1>
      <ul>
        {papers.map((paper) => {
          return (
            <li key={paper.id}>
              <h2>{paper.title}</h2>
              <p>{paper.abstract}</p>
            </li>
          );
        })}
      </ul>
    </main>
  );
}

export default App;
