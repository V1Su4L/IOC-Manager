import { useState, useEffect } from "react";
import axios from "axios";

type Report = {
  type: string;
  md5: string;
  sha1: string;
  sha256: string;
  last_analysis_stats: any;
  last_analysis_results: any;
};

function App() {
  const [report, setReport] = useState<Report | null>(null);
  const [hash, setHash] = useState("");

  const handleGenerateReport = () => {
    axios
      .post(`/virustotal/${hash}`)
      .then((response) => {
        setReport(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  useEffect(() => {
    if (hash === "") return;

    axios
      .get(`/virustotal/${hash}`)
      .then((response) => {
        setReport(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, [hash]);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setHash(event.target.value);
  };

  return (
    <div>
      <h1>Get VirusTotal Report</h1>
      <div>
        <label htmlFor="hash">Hash: </label>
        <input type="text" id="hash" value={hash} onChange={handleInputChange} />
        <button onClick={handleGenerateReport}>Generate Report</button>
      </div>
      {report ? (
        <div>
          <h2>Report for {hash}</h2>
          <ul>
            <li>Type: {report.type}</li>
            <li>MD5: {report.md5}</li>
            <li>SHA1: {report.sha1}</li>
            <li>SHA256: {report.sha256}</li>
            <li>Last Analysis Stats: {JSON.stringify(report.last_analysis_stats)}</li>
            <li>Last Analysis Results: {JSON.stringify(report.last_analysis_results)}</li>
          </ul>
        </div>
      ) : null}
    </div>
  );
}

export default App;
