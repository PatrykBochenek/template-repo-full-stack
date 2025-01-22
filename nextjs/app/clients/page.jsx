import { ENDPOINTS } from "@/config/endpoints"


export default async function Page(){
    const response = await fetch(ENDPOINTS.clients)
    const data = await response.json()
    return (
        <div className="p-6 ">
        <h1 className="text-2xl font-bold text-center text-gray-800">Client List</h1>
        <ul className="mt-6 space-y-4">
          {data.map((item) => (
            <li
              key={item.id}
              className="bg-white shadow rounded-lg p-4 hover:shadow-lg "
            >
              <h2 className="text-lg font-semibold text-blue-600">{item.code}</h2>
       
            </li>
          ))}
        </ul>
      </div>
      );
}