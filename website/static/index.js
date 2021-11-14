function deleteEntry(entryId) { // JS method to delete an entry
    fetch("/delete-entry", {
      method: "POST",
      body: JSON.stringify({ entryId: entryId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }