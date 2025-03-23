import React, { useState, useEffect } from "react";

const App = () => {
  const [users, setUsers] = useState([]);
  const [posts, setPosts] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const usersResponse = await fetch("https://jsonplaceholder.typicode.com/users");
        if (!usersResponse.ok) throw new Error("Ошибка при загрузке пользователей");
        const usersData = await usersResponse.json();
        setUsers(usersData);

        const postsResponse = await fetch("https://jsonplaceholder.typicode.com/posts");
        if (!postsResponse.ok) throw new Error("Ошибка при загрузке постов");
        const postsData = await postsResponse.json();
        setPosts(postsData);
      } catch (error) {
        console.error("Ошибка при загрузке данных:", error);
      }
    };

    fetchData();
  }, []);

  const filteredPosts = selectedUser
    ? posts.filter((post) => post.userId === selectedUser.id)
    : posts;

  console.log("Selected User:", selectedUser);
  console.log("Filtered Posts:", filteredPosts);

  return (
    <div style={{ display: "flex", padding: "20px" }}>
      <div style={{ width: "30%", marginRight: "20px" }}>
        <h2>Пользователи</h2>
        <ul style={{ listStyle: "none", padding: 0 }}>
          {users.map((user) => (
            <li
              key={user.id}
              style={{
                padding: "10px",
                margin: "5px 0",
                backgroundColor: selectedUser?.id === user.id ? "#ddd" : "#f4f4f4",
                cursor: "pointer",
              }}
              onClick={() => setSelectedUser(user)}
            >
              {user.name}
            </li>
          ))}
        </ul>
      </div>

      <div style={{ width: "70%" }}>
        <h2>Посты</h2>
        {filteredPosts.length > 0 ? (
          filteredPosts.map((post) => (
            <div
              key={post.id}
              style={{
                border: "1px solid #ccc",
                padding: "10px",
                margin: "10px 0",
                borderRadius: "5px",
              }}
            >
              <h3>{post.title}</h3>
              <p>{post.body}</p>
              <small>
                Автор:{" "}
                {users.find((user) => user.id === post.userId)?.name || "Неизвестно"}
              </small>
            </div>
          ))
        ) : (
          <p>Нет постов для отображения.</p>
        )}
      </div>
    </div>
  );
};

export default App;