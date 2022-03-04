import React, { Component } from 'react';
import axios from 'axios';

class UrlBar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            urlInput: '',
            sentiment: ''    
        };
    
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({urlInput: event.target.value});
    }
    
    handleSubmit(event) {
        let splitURL = this.state.urlInput.split('/')
        console.log(splitURL[6])

        let getURL = `/comments/${splitURL[6]}`

        console.log(getURL)

        axios.get(getURL)
            .then(res => {
                console.log(res)
                this.props.updateSentiment(res.data)
            })
            .catch((e) => {
                alert(`Failed to send get request\n${e}`)
            })

        event.preventDefault();
    }

    render() {
        return (
            <div>
                <h4>Paste the URL of the reddit thread you want to analyse.</h4>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        URL:
                        <input type="text" value={this.state.urlInput} onChange={this.handleChange} />
                    </label>
                    <input type="submit" value="Analyse" />
                </form>
            </div>
        )
    }
}

export default UrlBar;