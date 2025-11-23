import React from 'react';

const ResultsPanel = ({ results, loading }) => {
  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow-2xl p-6">
        <div className="flex items-center justify-center py-12">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
          <span className="ml-4 text-gray-600">Searching...</span>
        </div>
      </div>
    );
  }

  if (!results) return null;

  const renderResults = () => {
    if (!results.results) return null;

    const { results: data } = results;

    return (
      <div className="space-y-6">
        {/* Social Media Results */}
        {data.social_media && (
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4">Social Media Profiles</h3>
            {Object.entries(data.social_media).map(([platform, profiles]) => (
              <div key={platform} className="mb-4">
                <h4 className="font-semibold text-gray-700 capitalize mb-2">{platform}</h4>
                {profiles.length > 0 ? (
                  <div className="space-y-2">
                    {profiles.map((profile, idx) => (
                      <div key={idx} className="bg-gray-50 p-3 rounded border">
                        {profile.profile_url && (
                          <a
                            href={profile.profile_url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="text-blue-600 hover:underline"
                          >
                            {profile.username || profile.name || 'View Profile'}
                          </a>
                        )}
                        {profile.note && (
                          <p className="text-sm text-gray-500 mt-1">{profile.note}</p>
                        )}
                      </div>
                    ))}
                  </div>
                ) : (
                  <p className="text-gray-500 text-sm">No profiles found</p>
                )}
              </div>
            ))}
          </div>
        )}

        {/* Email Results */}
        {data.emails && (
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4">Email Addresses</h3>
            <div className="space-y-2">
              {data.emails.map((email, idx) => (
                <div key={idx} className="bg-gray-50 p-3 rounded border">
                  <pre className="text-sm">{JSON.stringify(email, null, 2)}</pre>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Phone Results */}
        {data.phones && (
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4">Phone Numbers</h3>
            <div className="space-y-2">
              {data.phones.map((phone, idx) => (
                <div key={idx} className="bg-gray-50 p-3 rounded border">
                  <pre className="text-sm">{JSON.stringify(phone, null, 2)}</pre>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Image Search Results */}
        {data.image && (
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4">Image Search Results</h3>
            <pre className="text-sm bg-gray-50 p-4 rounded overflow-auto">
              {JSON.stringify(data.image, null, 2)}
            </pre>
          </div>
        )}

        {/* WiFi Results */}
        {data.wifi && (
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4">WiFi Networks</h3>
            <pre className="text-sm bg-gray-50 p-4 rounded overflow-auto">
              {JSON.stringify(data.wifi, null, 2)}
            </pre>
          </div>
        )}

        {/* Raw Results */}
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-xl font-bold text-gray-800 mb-4">Raw Results</h3>
          <pre className="text-xs bg-gray-50 p-4 rounded overflow-auto max-h-96">
            {JSON.stringify(results, null, 2)}
          </pre>
        </div>
      </div>
    );
  };

  return (
    <div className="bg-white rounded-lg shadow-2xl p-6">
      <div className="mb-4">
        <h2 className="text-2xl font-bold text-gray-800">Search Results</h2>
        <p className="text-sm text-gray-600">
          Search ID: {results.search_id}
        </p>
        <p className="text-sm text-gray-600">
          Query: {results.query}
        </p>
      </div>
      {renderResults()}
    </div>
  );
};

export default ResultsPanel;

