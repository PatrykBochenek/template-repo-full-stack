import { PlusCircle, ChevronRight, Calendar, Users, Search } from 'lucide-react';

async function getData() {
  const response = await fetch('http://127.0.0.1:8000/clients');
  const data = await response.json();
  return data;
}

export default async function ClientDashboard() {
  const clients = await getData();

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-gray-800">Client Dashboard</h1>
        <button className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors">
          <PlusCircle size={20} />
          Add Client
        </button>
      </div>

      <div className="bg-white rounded-lg shadow-sm mb-6 p-6">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={20} />
          <input
            type="text"
            placeholder="Search clients..."
            className="pl-10 w-full border border-gray-200 rounded-lg py-2 px-4 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {clients.map((client) => (
          <div
            key={client.id}
            className="bg-white rounded-lg shadow-sm hover:shadow-lg transition-shadow cursor-pointer p-4"
          >
            <div className="flex items-center justify-between pb-2">
              <h2 className="text-xl font-bold">{client.code}</h2>
              <ChevronRight className="text-gray-400" />
            </div>
            <div>
              {client.name && (
                <p className="text-sm text-gray-500 mb-4">{client.name}</p>
              )}
              <div className="flex items-center justify-between text-sm">
                <div className="flex items-center gap-2">
                  <Calendar size={16} className="text-blue-500" />
                  <span>
                    {client.accounting_periods?.length || 0} Periods
                  </span>
                </div>
                <div className="flex items-center gap-2">
                  <Users size={16} className="text-green-500" />
                  <span>Active</span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {clients.length === 0 && (
        <div className="bg-gray-50 rounded-lg p-8 text-center">
          <p className="text-gray-600">No clients found.</p>
        </div>
      )}
    </div>
  );
}