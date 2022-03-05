import './SentimentBar.css';
import React, {Component} from 'react';

class SentimentBar extends Component {
    render() {
        return (
            <div className='progress-bar'>
                <div className='filler' style={{ marginLeft: `${this.props.sentimentPercent}%`}}/>
            </div>
        )
    }
}

export default SentimentBar;