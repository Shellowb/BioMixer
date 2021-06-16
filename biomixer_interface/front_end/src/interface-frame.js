import React, {Component} from "react";
import App from "./App";

class InterfaceFrame extends Component {

    render() {
        return (
            <div>
                {/* MENU */}
                <div className="navbar-dark text-white">
                    <div className="container">
                        <nav className="navbar px-0 navbar-expand-lg navbar-dark">
                            <button className="navbar-toggler" type="button" data-toggle="collapse"
                                    data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup"
                                    aria-expanded="false" aria-label="Toggle navigation">
                                <span className="navbar-toggler-icon"></span>
                            </button>
                            <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                                <div className="navbar-nav">
                                    <a href="/" className="pl-md-0 p-3 text-light">Home</a>
                                    <a href="/library/"
                                       className="p-3 text-decoration-none text-light">Library</a>
                                    <a href="/preparing/"
                                       className="p-3 text-decoration-none text-light">Prepare a Mix</a>
                                </div>
                            </div>
                        </nav>
                    </div>
                </div>
                <div id="body" className="container">
                    <h2>SOMETHING</h2>
                </div>
            </div>
        );
    }
}

export default InterfaceFrame;