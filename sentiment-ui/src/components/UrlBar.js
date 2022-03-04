import React, { Component } from 'react';
import axios from 'axios';

class UrlBar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
            sentiment: ''    
        };
    
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }
    
    handleSubmit(event) {
        let splitURL = this.state.value.split('/')
        console.log(splitURL[6])

        let getURL = `/comments/${splitURL[6]}`

        console.log(getURL)

        axios.get(getURL)
            .then(res => {
                console.log(res)
                this.setState({sentiment: res.Body})
            })
            .catch(() => {
                alert("Failed to send get request")
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
                        <input type="text" value={this.state.value} onChange={this.handleChange} />
                    </label>
                    <input type="submit" value="Analyse" />
                </form>
            </div>
        )
    }
}

export default UrlBar;