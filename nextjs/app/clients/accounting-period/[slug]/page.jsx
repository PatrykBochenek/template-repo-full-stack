import { ENDPOINTS } from "@/config/endpoints" 


export default async function Page({params}){
    const {slug} = params;
    const response = await fetch('http://127.0.0.1:8000/client-account/' + slug)
    const data = await response.json()
    
    return (
        <div className="p-6 ">
            <h1 className="text-2xl font-bold text-center text-gray-800">Client List</h1>
            {data.map((item) => (
                <div>{item.start_date}</div>
            ))}
        </div>

    );
    
}