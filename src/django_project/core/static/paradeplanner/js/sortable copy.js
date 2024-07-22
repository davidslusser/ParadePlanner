document.addEventListener("DOMContentLoaded", () => {
    const rowsPerPage = 5;
    let currentPage = 1;
    let currentSortColumn = null;
    let currentSortOrder = true; // true for ascending, false for descending

    const tableBody = document.querySelector("table tbody");
    const rows = Array.from(tableBody.querySelectorAll("tr"));
    const totalRows = rows.length;
    let sortedRows = rows.slice();

    const renderTable = (data, page = 1, rowsPerPage = 5) => {
        tableBody.innerHTML = "";
        const start = (page - 1) * rowsPerPage;
        const end = start + rowsPerPage;
        data.slice(start, end).forEach(row => tableBody.appendChild(row));
        renderPagination(data.length, page, rowsPerPage);
    };

    const renderPagination = (totalRows, page, rowsPerPage) => {
        const totalPages = Math.ceil(totalRows / rowsPerPage);
        const pagination = document.querySelector(".pagination");
        pagination.innerHTML = "";

        for (let i = 1; i <= totalPages; i++) {
            pagination.innerHTML += `
                <li class="page-item ${i === page ? 'active' : ''}">
                    <a class="page-link" href="#">${i}</a>
                </li>
            `;
        }

        document.querySelectorAll(".page-link").forEach(link => {
            link.addEventListener("click", (e) => {
                e.preventDefault();
                currentPage = parseInt(e.target.textContent);
                renderTable(sortedRows, currentPage, rowsPerPage);
            });
        });
    };

    const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;

    const comparer = (idx, asc) => (a, b) => ((v1, v2) =>
        v1 !== '' && v2 !== '' && !isNaN(v1) && !isNaN(v2) ? v1 - v2 : v1.toString().localeCompare(v2)
    )(getCellValue(asc ? a : b, idx), getCellValue(asc ? b : a, idx));

    document.querySelectorAll("th.sortable").forEach(th => th.addEventListener("click", () => {
        const idx = Array.from(th.parentNode.children).indexOf(th);
        const asc = !(currentSortColumn === idx && currentSortOrder);  // Toggle sort order

        currentSortColumn = idx;
        currentSortOrder = asc;

        sortedRows.sort(comparer(idx, asc));

        document.querySelectorAll('th.sortable').forEach(header => {
            header.classList.remove('asc', 'desc');
            header.querySelector('.fa-sort-up').classList.remove('sort-active');
            header.querySelector('.fa-sort-down').classList.remove('sort-active');
        });

        th.classList.toggle('asc', asc);
        th.classList.toggle('desc', !asc);
        if (asc) {
            th.querySelector('.fa-sort-up').classList.add('sort-active');
            th.querySelector('.fa-sort-down').classList.remove('sort-active');
        } else {
            th.querySelector('.fa-sort-up').classList.remove('sort-active');
            th.querySelector('.fa-sort-down').classList.add('sort-active');
        }

        currentPage = 1;  // Reset to the first page after sorting
        renderTable(sortedRows, currentPage, rowsPerPage);
    }));

    renderTable(sortedRows, currentPage, rowsPerPage);
});
