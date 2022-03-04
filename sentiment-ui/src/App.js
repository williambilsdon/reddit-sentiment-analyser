import './App.css';
import React, { Component } from 'react';
import UrlBar from './components/UrlBar';

class App extends  Component {
  state = {sentiment: ''}

  updateSentiment = (sentiment) => {
    this.setState({sentiment: sentiment})
  }

  render() {
    return (
      <div className="App">
        <h1>Reddit Football Sentiment Analyser</h1>
        <UrlBar updateSentiment={this.updateSentiment}/>
        <p>{this.state.sentiment}</p>
      </div>
    );
  }
}

export default App;
