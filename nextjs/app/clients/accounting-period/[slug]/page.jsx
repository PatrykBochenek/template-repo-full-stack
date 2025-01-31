import { Calendar, Search, ArrowLeft, PlusCircle } from 'lucide-react';
import Link from 'next/link';

export default async function Page({params}) {
    const {slug} = params;
    const response = await fetch('http://127.0.0.1:8000/clients/accounting-period/' + slug)
    const result = await response.json()
    const data = result.data || [];

    return (
        <div className="p-6 max-w-6xl mx-auto">
            <div className="flex items-center gap-4 mb-8">
                <Link href="/clients" className="text-gray-500 hover:text-gray-700">
                    <ArrowLeft size={24} />
                </Link>
                <div className="flex justify-between items-center w-full">
                    <h1 className="text-3xl font-bold text-gray-800">Client Dashboard</h1>
                    <Link href={`/clients/accounting-period/${slug}/create`} className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors">
                        <PlusCircle size={20} />
                        Add Accounting Period
                    </Link>
                </div>
            </div>

            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                {data.map((period) => (
                    <div key={period.id} className="bg-white rounded-lg shadow-sm hover:shadow-lg transition-shadow p-4">
                        <div className="flex items-center justify-between pb-2">
                            <h2 className="text-xl font-bold">Period {period.id}</h2>
                        </div>
                        <div>
                            <div className="flex items-center gap-2 text-sm text-gray-500 mb-2">
                                <Calendar size={16} className="text-blue-500" />
                                <span>Start: {new Date(period.start_date).toLocaleDateString()}</span>
                            </div>
                            <div className="flex items-center gap-2 text-sm text-gray-500">
                                <Calendar size={16} className="text-green-500" />
                                <span>End: {new Date(period.end_date).toLocaleDateString()}</span>
                            </div>
                        </div>
                        <div className="flex mt-3 items-center gap-2 text-sm text-gray-500 mb-2">
                            <span>Status: {period.status}</span>
                        </div>
                        <div className="flex mt-3 items-center gap-2 text-sm text-gray-500 mb-2">
                            <span>Bookkeeping Software: {period.bookkeeping_system}</span>
                        </div>
                    </div>
                ))}
            </div>

            {data.length === 0 && (
                <div className="bg-gray-50 rounded-lg p-8 text-center">
                    <p className="text-gray-600">No accounting periods found.</p>
                </div>
            )}
        </div>
    );
}