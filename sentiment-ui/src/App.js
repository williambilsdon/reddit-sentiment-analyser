import './App.css';
import React, { Component } from 'react';
import UrlBar from './components/UrlBar';
import SentimentBar from './components/SentimentBar';

class App extends  Component {
  state = {sentiment: 0}

  updateSentiment = (sentiment) => {
    this.setState({sentiment: sentiment})
  }

  render() {
    return (
      <div className="App">
        <h1>Reddit Comment Sentiment Analyser</h1>
        <UrlBar updateSentiment={this.updateSentiment}/>
        <SentimentBar sentimentPercent={this.state.sentiment}/>
      </div>
    );
  }
}

export default App;
